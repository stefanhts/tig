import sys, getopt, os, shutil, errno
from pathlib import Path
from datetime import datetime

# tig will take arguments from the command line. 
# The format should look something like:
# tig get dirname > this will pull the newest version of dir from the server
# tig create > this will mark the directory as a valid tig project
# tig push name > this will push changes to the dir to the server with the given name
# possibly implement tig pull specific > this will pull specific version

CREATE = 'create'
GET = 'get'
PUSH = 'push'
SERVER = '/home/stefanh/Documents/Projects/Temp2'
AUTHOR = 'stefanhts'
DATE = datetime.now() 
CHANGESET = 'init'
CWD = os.getcwd()
PARENT = CWD.split('/')[-1]

def create():
    try:
        f = open(".tig", "x")
        f.close()
        f = open(".tig", "w")
        f.write(f"CHANGESET={CHANGESET}\n")
        f.write(f"DATE={DATE}\n")
        f.write(f"AUTHOR={AUTHOR}\n")
        f.close()

    except:
        print ('Directory is already tig ready')

def push(dirname):
    text = f"CHANGESET={dirname}\nDATE={DATE}\nAUTHOR={AUTHOR}"
    f = open(".tig", "w")
    f.write(text)
    f.close()
    destination = f"{SERVER}/{PARENT}"
    try:
        os.mkdir(destination)
    except:
        None
    os.chdir(destination)
    #os.mkdir(f"{SERVER}/{PARENT}")
    copy()

def copy():
    # Check if dir exists before writing to it
    try:
        shutil.copytree(CWD, PARENT)
    except OSError as exc:
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(CWD, PARENT)
        else:
            print(exc)
        

def get(projname):
    print('project: ' +projname+' has been fetched')

def pull():
    print('fetched lated version')

def main(argv):
    _, args = getopt.getopt(argv, "", "")
    try:
        if args[0] == CREATE:
            if len(args) > 1:
                CHANGESET = args[1]
            create()
        elif args[0] == GET:
            get(args[1])
        elif args[0] == PUSH:
            print(args[0])
            push(args[1])
        else:
            print('incorrect arguments... tig -h for help')
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main(sys.argv[1:])



