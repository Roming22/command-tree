"""
Handles image build process.
"""


def get_argparser(parser):
    """
    Add command options
    """
    parser.add_argument("-d", dest="dockerfile")


def pre(context):
    """
    Handles the setup of the plugin
    """
    print("Hello from", __file__)
    return context


def run(context):
    """
    main function
    """
    print("Building", __file__)
    return context


def post(context):
    """
    Handles the teardown of the plugin
    """
    print("Bye from", __file__)
    return context
