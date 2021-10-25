import sys, getopt, os, shutil, errno
from pathlib import Path
from datetime import datetime

# tig will take arguments from the command line. 
# The format should look something like:
# tig get dirname > this will pull the newest version of dir from the server
# tig create > this will mark the directory as a valid tig project
# tig push name > this will push changes to the dir to the server with the given name
# possibly implement tig pull specific > this will pull specific version

_create = 'create'
_get = 'get'
_push = 'push'
_server = '/home/stefanh/Documents/Projects/Temp2'
_author = 'stefanhts'
_date = datetime.now() 
_changeset = 'init'
_cwd = os.getcwd()
_parent = _cwd.split('/')[-1]
_newest = "TODO"

def create():
    try:
        f = open(".tig", "x")
        f.close()
        f = open(".tig", "w")
        f.write(f"CHANGESET={_changeset}\n")
        f.write(f"DATE={_date}\n")
        f.write(f"AUTHOR={_author}\n")
        f.close()
    except:
        print ('Directory is already tig ready')

def push(dirname):
    # update the .tig file on each push
    text = f"CHANGESET={dirname}\nDATE={_date}\nAUTHOR={_author}"
    f = open(".tig", "w")
    f.write(text)
    f.close()
    destination = f"{_server}/{_parent}"
    # make sure the directory exists
    try:
        os.mkdir(destination)
    except:
        None
    # change to remote dir
    os.chdir(destination)
    copy(dirname)

def copy(dirname):
    # attempt to recursive copy the directory
    src = os.getcwd()
    try:
        shutil.copytree(src, dirname)
    except OSError as exc:
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dirname)
        else:
            print(exc)
        

def get(projname, version=_newest):
    # TODO: figure out how to handle multiple versions, maybe a meta file?
    src = f"{_server}/{projname}"
    print("src:...", src)
    try:
        None
        #os.mkdir(f"{_cwd}/{version}")
    except Exception as e:
        print(e)
    os.chdir(src)
    print("cwd: %s", src)
    copy(_cwd+"/"+version+"/")

    print('project: ' +projname+' has been fetched')

def pull():
    print('fetched lated version')

def main(argv):
    _, args = getopt.getopt(argv, "", "")
    try:
        if args[0] == _create:
            if len(args) > 1:
                CHANGESET = args[1]
            create()
        elif args[0] == _get:
            get(args[1],args[2])
        elif args[0] == _push:
            print(args[0])
            push(args[1])
        else:
            print('incorrect arguments... tig -h for help')
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main(sys.argv[1:])



