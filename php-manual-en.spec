# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The PHP Manual in the English language
Name:		php-manual-en
Version:	5.5.7
Release:	1
Group:		Books/Other
License:	PHP License
URL:		http://www.php.net/download-docs.php
Source:		http://fr2.php.net/distributions/manual/php_manual_en.tar.gz
Requires:       apache-mod_php
BuildArch:	noarch

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
install -d %{buildroot}%{_docdir}/%{name}
cp -aRf php-chunked-xhtml/* %{buildroot}%{_docdir}/%{name}/

install -d %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{name}.conf << EOF
Alias /%{name} %{_docdir}/%{name}

<Directory %{_docdir}/%{name}>
    Require all granted
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

%files
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%config(noreplace) %{_webappconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 5.4.4-1mdv2012.0
+ Revision: 806392
- 5.4.4

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 5.3.9-1
+ Revision: 761193
- 5.3.9

* Mon Mar 21 2011 Oden Eriksson <oeriksson@mandriva.com> 5.3.6-1
+ Revision: 647237
- 5.3.6

* Tue Jan 18 2011 Oden Eriksson <oeriksson@mandriva.com> 5.3.5-1
+ Revision: 631567
- new manual
- added menu stuff, apache and php ini sections

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 5.3.2-2mdv2011.0
+ Revision: 588736
- 5.3.3

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 5.3.2-1mdv2010.1
+ Revision: 514493
- 5.3.2

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 5.3.1-1mdv2010.1
+ Revision: 468101
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 5.3.1-0.0.RC1.1mdv2010.0
+ Revision: 451501
- new manual

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 5.2.9-2mdv2010.0
+ Revision: 397549
- Rebuild

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 5.2.9-1mdv2009.1
+ Revision: 346387
- 5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 5.2.9-0.0.RC2.1mdv2009.1
+ Revision: 341475
- 5.2.9RC2

* Wed Jan 14 2009 Oden Eriksson <oeriksson@mandriva.com> 5.2.8-1mdv2009.1
+ Revision: 329457
- 5.2.8

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 5.2.7-1mdv2009.1
+ Revision: 310232
- 5.2.7

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 5.2.6-1mdv2009.0
+ Revision: 237752
- 5.2.6

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.4-1mdv2008.0
+ Revision: 81530
- 5.2.4 (cosmetic release in most cases)

* Sat Jun 02 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.3-1mdv2008.0
+ Revision: 34519
- 5.2.3

* Mon May 07 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.2-1mdv2008.0
+ Revision: 24114
- 5.2.2


* Tue Feb 13 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.0
+ Revision: 120493
- Import php-manual-en

* Tue Feb 13 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.1
- 5.2.1

* Mon Sep 18 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1mdv2007.0
- 5.1.6

* Mon May 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-1mdk
- 5.1.4

* Tue May 02 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-1mdk
- 5.1.2

* Fri Dec 02 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-1mdk
- new release

* Tue Nov 01 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-1mdk
- new release

* Mon Jun 13 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- new release

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10-1mdk
- new release
- drop locales deps, it's not required...

* Tue Nov 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.9-1mdk
- initial mandrake package




