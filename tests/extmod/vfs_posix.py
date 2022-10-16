# Test for VfsPosix

try:
    import uos

    uos.VfsPosix
except (ImportError, AttributeError):
    print("SKIP")
    raise SystemExit

# We need a directory for testing that doesn't already exist.
# Skip the test if it does exist.
temp_dir = "micropy_test_dir"
try:
    uos.stat(temp_dir)
    print("SKIP")
    raise SystemExit
except OSError:
    pass

# getcwd and chdir
curdir = uos.getcwd()
uos.chdir("/")
print(uos.getcwd())
uos.chdir(curdir)
print(uos.getcwd() == curdir)

# stat
print(type(uos.stat("/")))

# listdir and ilistdir
print(type(uos.listdir("/")))

# mkdir
uos.mkdir(temp_dir)

with open(f"{temp_dir}/test", "w") as f:
    f.write("hello")
# close on a closed file should succeed
f.close()

# construct a file object using the type constructor, with a raw fileno
f = type(f)(2)
print(f)

with open(f"{temp_dir}/test", "r") as f:
    print(f.read())
# rename
uos.rename(f"{temp_dir}/test", f"{temp_dir}/test2")
print(uos.listdir(temp_dir))

# construct new VfsPosix with path argument
vfs = uos.VfsPosix(temp_dir)
print([i[0] for i in vfs.ilistdir(".")])

# stat, statvfs
print(type(vfs.stat(".")))
print(type(vfs.statvfs(".")))

# check types of ilistdir with str/bytes arguments
print(type(list(vfs.ilistdir("."))[0][0]))
print(type(list(vfs.ilistdir(b"."))[0][0]))

# remove
uos.remove(f"{temp_dir}/test2")
print(uos.listdir(temp_dir))

# remove with error
try:
    uos.remove(f"{temp_dir}/test2")
except OSError:
    print("remove OSError")

# rmdir
uos.rmdir(temp_dir)
print(temp_dir in uos.listdir())

# rmdir with error
try:
    uos.rmdir(temp_dir)
except OSError:
    print("rmdir OSError")
