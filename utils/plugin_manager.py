'''
Load plugins from a specified directory.
It is up to the program to ensure that the plugins implement the proper interfaces.
'''

import imp
import os.path
import sys


def load_from(plugins_dir):
    '''
    Loads plugins located in plugins_dir
    '''
    plugins = {}
    plugins_dir = os.path.abspath(plugins_dir)

    if not os.path.isdir(plugins_dir):
        return plugins

    for filename in os.listdir(plugins_dir):
        file_path = os.path.join(plugins_dir, filename)
        if os.path.isfile(file_path) and filename.endswith(".py") and filename != "__init__.py":
            module_name = filename.split(".")[0]
            module_info = imp.find_module(module_name, [plugins_dir])
            imp.load_module(module_name, *module_info)
            sys.modules[module_name].plugins = load_for(file_path)
            plugins[module_name] = sys.modules[module_name]
    return plugins


def load_for(filepath):
    '''
    Returns the expected directory where plugins are to be found.
    '''
    module_dir = os.path.dirname(os.path.abspath(filepath))
    module_name = os.path.basename(filepath).split('.')[0]
    return load_from(os.path.join(module_dir, module_name))


def get_argparser(parser, plugins, level=2):
    '''
    Generate the argument parser for all plugins
    '''
    for name, plugin in plugins.iteritems():
        subparser = parser.add_parser(name)
        plugin.get_argparser(subparser)
        if plugin.plugins:
            subparsers = subparser.add_subparsers(dest='command' + str(level))
            get_argparser(subparsers, plugin.plugins, level + 1)
