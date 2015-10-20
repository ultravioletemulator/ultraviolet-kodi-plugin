
sudo dpkg -r ultraviolet
sudo dpkg -i ultraviolet-0.1-alpha.deb

echo "Check license"
dpkg-deb --fsys-tarfile ultraviolet-0.1-alpha.deb |tar -xvO ./usr/share/doc/ultraviolet/copyright


echo "http://www.aptly.info/"
echo "Probatu aptly debian-en publikatzeko..."
