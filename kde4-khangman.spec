%define		_state		stable
%define		orgname		khangman

Summary:	K Desktop Environment - A hangman game
Summary(pl.UTF-8):	K Desktop Environment - Gra w wisielca
Name:		kde4-khangman
Version:	4.14.3
Release:	3
License:	GPL
Group:		X11/Applications/Science
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	52108ad0becfca7c39700aa46540d480
Patch0:		x32.patch
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdeedu-devel >= %{version}
Obsoletes:	kde4-kdeedu-khangman < 4.6.99
Obsoletes:	khangman <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter after another. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description -l pl.UTF-8
KHangMan jest grą opartą na popularnej grze w wisielca. Wybierane jest
losowe słowo, którego litery są ukryte. Trzeba zgadnąć to słowo
podając kolejno litery. Za każdym razem, gdy podana litera nie
występuje w słowie, rysowany jest obrazek wisielca. Trzeba odgadnąć
słowo przed powieszeniem! Gra jest przeznaczona dla dzieci w wieku 6
lat lub więcej.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%attr(755,root,root) %{_libdir}/libkhangmanengine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkhangmanengine.so.?
%{_datadir}/appdata/khangman.appdata.xml
%{_datadir}/apps/khangman
%{_datadir}/config.kcfg/khangman.kcfg
%{_datadir}/config/khangman.knsrc
%{_desktopdir}/kde4/khangman.desktop
%{_iconsdir}/hicolor/scalable/apps/khangman*.svgz
%{_iconsdir}/hicolor/*x*/apps/khangman*.png
%{_mandir}/man6/khangman.6*
