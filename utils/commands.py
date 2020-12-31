"""Utility class for registering fire CLI commands."""


class CommandRegistry:
    """Command Registry singleton, used to register and retrieve commands."""

    __instance = None
    _registry = {}

    @staticmethod
    def getInstance():
        """Get singleton instance."""
        if CommandRegistry.__instance is None:
            CommandRegistry()
        return CommandRegistry.__instance

    def __init__(self):
        """Instantiate command registry."""
        if CommandRegistry.__instance is not None:
            raise 'CommandRegistry should not be instantiated.'
        else:
            CommandRegistry.__instance = self

    @staticmethod
    def register(commands: dict):
        """Register a command.

        Args:
            commands (dict): dictionary of commands and functions to service commands
            e.g. {
                'foo': {
                    'bar': my_foobar_command
                }
            }
            fulmar foo bar --foobar_arg1 --foobar_arg2
        """
        for k, v in commands.items():
            if isinstance(v, dict) and k in CommandRegistry.getInstance()._registry:
                CommandRegistry.getInstance()._registry[k].update(v)
            else:
                CommandRegistry.getInstance()._registry[k] = v

    @staticmethod
    def commands():
        """Get registered commands.

        Returns:
            dict: fire compatible command dictionary
        """
        r = CommandRegistry.getInstance()._registry
        r['__doc__'] = 'Available commands:\r\n{0}\r\nUse --help for further details.'.format('\r\n'.join(r.keys()))
        return r
