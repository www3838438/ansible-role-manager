import os, shutil
from . import Command
from arm.util import retrieve_role, get_playbook_root, retrieve_all_roles

class BaseCommand(Command):
        
    help = "install playbook role"    
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('-U','--upgrade', action='store_true')
        parser.add_argument('-n', '--no-dependencies', action='store_true')
        parser.add_argument('role', help='name of the role to install')
        
    def run(self, argv):
        
        role_ident = argv.role
        root = get_playbook_root(os.getcwd())
        if not root:
            print '''
            can't find playbook. 
            use `arm init` to create recommended structure.
            or use the `--no-dependencies` option.'''
            return 1
        
        roles = []
        if argv.no_dependencies:
            role = retrieve_roll(roll_ident)
            roles = [ role, ]
        else:
            roles = retrieve_all_roles(role_ident)

        alias = name # TODO unless #aliasname or #alias=aliasname

        # this needs to be converted to handling multiple roles
        # for role in roles:
        #    name = role.get_name()
        #    alias = name if not #alias but only applies to the first role, should assert that's the first in the role list)
        
        library = os.path.join(root,'library_roles',name)
        destination = os.path.join(root, 'roles', alias)
        
        if os.path.exists(library):
            
            if os.path.exists(destination) and not os.path.islink(destination) and not getattr(argv, 'upgarde', False):
                print "role '%s' already exists as a non-library role"
                return 1            
            
            if getattr(argv, 'upgrade', False):
                if os.path.exists(library): shutil.rmtree(library)
                if os.path.islink(destination):
                    print "unlinking: %s" % destination
                    os.unlink(destination)
            else:
                print "existing version already installed in library, use --upgrade to install latest"
                return 1                
                
        shutil.copytree(source, library)
        
        
        os.symlink(
            os.path.relpath(destination, 'roles/'),
            os.path.join('roles',os.path.basename(alias))
            )
        print "role '%s' installed succesfully" % (argv.role)
        return 0
                
        
        

        
        
