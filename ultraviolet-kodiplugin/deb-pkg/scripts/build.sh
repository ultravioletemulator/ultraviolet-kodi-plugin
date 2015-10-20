
echo "Creating man files ..."

gzip --best ./pkg/usr/share/man/man1/ultraviolet.1

echo "Building package ..."
dpkg-deb --build pkg
mv pkg.deb ultraviolet-0.1-alpha.deb
