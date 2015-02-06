Name:		callgit
Version:	2.1
Release:	2
Summary:	A tool for Ham Radio Operators to look up call-signs on the web
Group:		Communications
License:	GPLv3
URL:		http://www.hamsoftware.org/
Source0:	http://www.hamsoftware.org/%{name}-%{version}.tgz
#Icon from Fedora
Source1:	Ham_Icon-1-48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	qt4-devel

%description
This program allows you to search for another Ham's name and address
without having a web browser up. It is very simple.

%prep
%setup -q -n %{name}

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
install -Dpm 755 callgit %{buildroot}/%{_bindir}/%{name}

#icon
install -Dpm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/Ham_icon_callgit.png

#desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CallGit
Comment=Ham Radio call-sign lookup tool
Exec=callgit
Icon=Ham_icon_callgit
Terminal=false
Type=Application
Categories=Qt;Network;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/Ham_icon_callgit.png
