


@click.command()
@click.argument('filename')
@click.argument('actions', nargs=-1)
@click.option('--listpaths', '-l', is_flag=True, 
    help='List available metric pathnames in the FILENAME')
@click.option('--timerange', '-t', type=str, default=None, 
    help='Date & time range to process, e.g. YYYYMMDDHHMM:YYYYMMDDMM or -0400:')
@click.option('--verbose', '-v', is_flag=True)
@click.option('--debug', '-d', is_flag=True)
def cli(**args):
    """
    \b
    Produce charts for data FILENAME using ACTION(s)
    Actions can be a mixture of script names and arguments in the form x=y:
    \b
    Stock scripts;
        - healthcheck (default)
        - topports
        - ldevtop
        - hur
    """
    global DEBUG
    DEBUG = True if args['debug'] else False
    if DEBUG: print('DEBUG is enabled')
    if DEBUG: print('args:', args)
    global VERBOSE
    VERBOSE = True if args['verbose'] else False
    filename = args['filename']
    actionlist = args['actions'] 
    listpaths = args['listpaths']
    timerange = args['timerange']