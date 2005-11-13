Summary:	e16menuedit - menu editor for Enlightenment
Summary(pl):	e16menuedit - edytor menu dla Enlightenmenta
Name:		e16menuedit
Version:	0.1.3
Release:	1
License:	MIT-like
Group:		X11/Window Managers/Tools
Source0:	http://ftp.debian.org/debian/pool/main/e/e16menuedit/%{name}_%{version}.orig.tar.gz
# Source0-md5:	737e41343a99256dd66dfae2c21bc375
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e16menuedit is a GTK+ based program that allows configuration of menus
for the Enlightenment window manager.

%description -l pl
e16menuedit to oparte na GTK+ narzêdzie umo¿liwiaj±ce konfiguracjê
menu dla zarz±dcy okien Enlightenment.

%prep
%setup -q -n %{name}-%{version}.orig

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install	e16menuedit	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
