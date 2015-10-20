rm -rf ./usr/lib/python3.4/*
rm -rf ./usr/share/man/*

mkdir -p ./usr/lib/python3.4
cp -r /home/developer/python/workspace/ultraviolet-emulator/git/ultraviolet-kodi-plugin/ultraviolet-kodiplugin/src/* ./usr/lib/python3.4/

# mkdir ./usr/share
# mkdir ./usr/share/man
mkdir -p ./usr/share/man/man1
cp /home/developer/python/workspace/ultraviolet-emulator/git/ultraviolet-kodi-plugin/ultraviolet-kodiplugin/deb-pkg/man/ultraviolet.1 ./usr/share/man/man1/ultraviolet.1
find ./ -type d | xargs chmod 755
