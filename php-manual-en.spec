# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The PHP Manual in the English language
Name:		php-manual-en
Version:	5.3.5
Release:	%mkrel 1
Group:		Books/Other
License:	PHP License
URL:		http://www.php.net/download-docs.php
Source:		http://fr2.php.net/distributions/manual/php_manual_en.tar.gz
Requires:       apache-mod_php
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d %{buildroot}%{_docdir}/%{name}
cp -aRf php-chunked-xhtml/* %{buildroot}%{_docdir}/%{name}/

install -d %{buildroot}%{webappconfdir}
cat > %{buildroot}%{webappconfdir}/%{name}.conf << EOF
Alias /%{name} %{_docdir}/%{name}

<Directory %{_docdir}/%{name}>
    Order Allow,Deny
    Allow from All
</Directory>
EOF

install -d %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/%{name}.ini << EOF
docref_root = /%{name}/
docref_ext = .html
EOF

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=The PHP %{version} HTML manual in English
Comment=The PHP %{version} HTML manual in English
Exec=%{_bindir}/www-browser %{_docdir}/%{name}/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%config(noreplace) %{webappconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{_datadir}/applications/%{name}.desktop
