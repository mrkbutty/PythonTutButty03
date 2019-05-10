# print activetot pages for lanes (policies) of dpsnapout.txt
# summarize TI PVOL usage

BEGIN {
	freqflag=0
	tiercount=0
	tiertotal=0
	tierused=0
	section=0
	lastldev=""
	ldevsize=0
	tistatushead=0
	tisizehead=0
	tistatusout=".tistatus.out.csv"
	tisizeout=".tisize.out.csv"
	totalsnapsize=0
}

     function round(x,   ival, aval, fraction)  {
        ival = int(x)    # integer part, int() truncates
     
        # see if fractional part
        if (ival == x)   # no fraction
           return ival   # ensure no decimals
     
        if (x < 0) {
           aval = -x     # absolute value
           ival = int(aval)
           fraction = aval - ival
           if (fraction >= .5)
              return int(x) - 1   # -2.5 --> -3
           else
              return int(x)       # -2.3 --> -2
        } else {
           fraction = x - ival
           if (fraction >= .5)
              return ival + 1
           else
              return ival
        }
     }

function summary() {

	if (length(tierPages) > 1) {
		print "< Tier Sizing >"
		for (i in tierPages) {
			if (tierPages[i] > 0 && tierPotential[i] > 0) piophpp=round(tierPotential[i] / tierPages[i])
			else piophpp=0
			percent = (tierPages[i] / tiertotal) * 100
			
			printf "%13s = %-3.1f%%    Potential-IOPH-per-Page = %d\n", i, percent, piophpp
		}
		if (tiertotal > 0 && tierused > 0) pused = (tierused/tiertotal) * 100
		else pused=0
		print "      ------------------------------------------------------------"
		printf "          Total Pages = %d  Used = %d (%3.1f%%)", tiertotal, tierused, pused
		print "\n"
	}
	
	print "< Lane Summary >"
	printf "%6s %14s %14s %14s %14s %14s\n", "Policy", "Active-Pages", "Inactive-Pages", "Used-Pages", "Total-IOPH", "Access-Density"

	num=asorti(activetot,keys)
	for (i=1; i<=num; i++) {
		totpages=activetot[keys[i]]+zerotot[keys[i]]
		if ( activetot[keys[i]] > 0 && totIOPH[keys[i]] > 0 ) access = totIOPH[keys[i]] / activetot[keys[i]]
		else access=0

		printf "%6s %14d %14d %14d %14d %14.2f\n", keys[i], activetot[keys[i]], zerotot[keys[i]], totpages, totIOPH[keys[i]], access
	}
	printf "\n"
	print "< Potential IOPH by Lane & Tier >"
	printf "    Lane-Policy"
	for (j=1; j<=tiercount; j++) printf " %14s", tiername[j]
	printf "\n"
	for (i=1; i<=num; i++) {
		totpages=activetot[keys[i]]+zerotot[keys[i]]
		printf " %14s", keys[i]
		for (j=1; j<=tiercount; j++) {
			tier=tiername[j]
			if (tierPages[tier] > 0 && tierPotential[tier] > 0) piophpp=round(tierPotential[tier] / tierPages[tier])
			else piophpp=0
			pioph=totpages*piophpp
			percent=pioph/(tierPotential[tier]/100)
			printf " %13d%%", percent
			#printf "\n  %d   %d   \n", pioph, tierPotential[tier]
		}
		printf "\n"
	}
	printf "\n"
	
	delete activetot
	delete zerotot
	delete totIOPH
	delete tierPotential
	delete tierPages
	tiercount=0
	tiertotal=0
	tierused=0
}

/^[ \t]*$/ { section=0 }   # reset on blank line

/^(DP.*|TI.*)/ {
	pooltype=$0
}


/^ *POOL-ID *:/ { 
	if (freqflag) summary()
	print $0 " " pooltype
	freqflag=0
	ticount=0
}

/Status/ { 
	section=1  # header
}

/.*:/ {
	if (section==1) { 
		if ($0 !~ / +0\[|No data|No Setting/) {
			print
		}
	}
}


/^ +Total Size/ { 
	match($0, /Total.*: +([0-9]+).*/, result)
	pooltotMB=result[1]
	#print "result0=" result[0]
	#print "total=[" pooltotMB "]"
}

/Monitor information/,/^ *$/ { 
	print 
	if ($3 ~ /[0-9]+/ && $4 ~ /[0-9]+/) tierPotential[$2]=$4
}

/Tier range/,/^ *$/ { print }

/Page assignment/,/^ *$/ { 
	if ($2 ~ /[0-9]+/ && $3 ~ /[0-9]+/) { 
		tiercount++
		tierPages[$1]=$3
		tiername[tiercount]=$1
		tiertotal+=$3
		tierused+=$2
		print $0
	}
	else print
}

/Frequency distribution information/,/^ *$/ {
	freqflag=1
	
	if($0 ~ /^ *ALL|^ *LV[0-9]/) {
		level=$1
		pages=$5
		ioph=$6
		
		if (!level in activetot) activetot[level]=0
		if (!level in totIOPH) totIOPH[level]=0
		if (!level in zerotot) zerotot[level]=0
		if (ioph > 0) activetot[level]=activetot[level]+pages
		else zerotot[level]=zerotot[level]+pages
		totIOPH[level]=totIOPH[level]+ioph
		
		
		#printf "%s\t%d\t%d\n", level, pages, ioph
	}
}

/^ *P-VOL/  { print "Total number of TI PVOLs =" $0 }

/S-VOL/,/^ *$/ {
	#rc = match($0, /^\s+(0x[0-9A-F]+)\s+S-VOL/, result)
	if($0 ~ /S-VOL/) {
		pvol=$1
		#print "PVOL is" pvol
	}
	else if($0 ~ / +0x.*/) {
		pstatus=$2
		if (!pstatus in pstatuscount) pstatuscount[pstatus]=0
		if (!pstatus in titotalcount) titotalcount[pstatus]=0
		pstatuscount[pstatus]++
		titotalcount[pstatus]++
	}
	else if($0 ~ /^ *$/){
		num=asorti(pstatuscount,keys)
		for (i=1; i<=num; i++) {
			if(tistatushead==0) {
				printf "PVol,Status,Count\n" > (FILENAME tistatusout)
				tistatushead=1
				print "Writing", (FILENAME tistatusout)
			}
			printf "%s,%s,%d\n", pvol, keys[i], pstatuscount[keys[i]] > (FILENAME tistatusout)
		}
		delete pstatuscount
	}

}


/CVDEV info/,/^ *$/ {
	if($0 ~ / *0x.*TI/) {
		ldev=$1
		if(ldev != lastldev) {
			if(tisizehead==0) {
				printf "PVol,size MB\n" > (FILENAME tisizeout)
				tisizehead=1
				print "Writing", (FILENAME tisizeout)
			}
			if(length(lastldev) > 0) { printf "%s,%s\n", lastldev, ldevsize > (FILENAME tisizeout) }
			lastldev=ldev
			ldevsize=0
		}
		ldevsize+=$4
		totalsnapsize+=$4
	}
	else if($0 ~ /^ *$/) {
		if(length(lastldev) > 0) {
			printf "%s,%s\n", lastldev, ldevsize > (FILENAME tisizeout)
		}
		lastldev=""
		ldevsize=0
	}
}


END {
	if (freqflag) summary()

	num=asorti(titotalcount,keys)
	if(num > 0) {
		titot=0
		for (i=1; i<=num; i++) {
			printf "Total number of snapshots with status %s = %d\n", keys[i], titotalcount[keys[i]]
			titot+=titotalcount[keys[i]]
		}
		printf "Total number of snapshots = %d\n", titot
	}
	if(totalsnapsize > 0) {
		printf "Total snapshots size = %d GB\n", (totalsnapsize/1024)
	}
}