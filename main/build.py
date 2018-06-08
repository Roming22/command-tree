'''
Handle the build step and build options.
The process is delegated to objects plugins.
'''


def get_argparser(parser):
    '''
    Add command options
    '''
    parser.add_argument('-n', dest='dryrun')


def pre(context):
    '''
    Handles the setup of the plugin
    '''
    print "Hello from", __file__
    return context


def post(context):
    '''
    Handles the teardown of the plugin
    '''
    print "Bye from", __file__
    return context
