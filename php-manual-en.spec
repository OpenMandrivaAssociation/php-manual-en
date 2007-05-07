# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The PHP Manual in the English language
Name:		php-manual-en
Version:	5.2.2
Release:	%mkrel 1
Group:		Books/Other
License:	PHP License
URL:		http://www.php.net/download-docs.php
Source:		http://fr2.php.net/distributions/manual/php_manual_en.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
The PHP Manual in the English (en) language.

%prep

%setup -q -c -n php_manual_en

# fix perms
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# clean up cvs junk		
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}/var/www/html/addon-modules
pushd %{buildroot}/var/www/html/addon-modules
    ln -s  ../../../..%{_docdir}/php-manual-en-%{version} php-manual-en-%{version}
popd

find | sed 's/^/%doc /' | grep -v '\./%{name}.filelist' > %{name}.filelist

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root,root)
/var/www/html/addon-modules/php-manual-en*


