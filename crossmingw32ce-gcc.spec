#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingw)
#
Summary:	Cross Mingw32CE GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - Mingw32CE gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - Mingw32CE gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla Mingw32CE - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - Mingw32CE gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - Mingw32CE gcc
Name:		crossmingw32ce-gcc
Version:	4.1.0
Release:	0.1
License:	GPL
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# https://cegcc.svn.sourceforge.net/svnroot/cegcc/trunk/cegcc/src/gcc
Source0:	gcc-20070227.909.tar.bz2
# Source0-md5:	ece53d2ea4d055f48d4f819922332d21
Patch0:		gcc-nodebug.patch
Patch1:		%{name}-bug25672.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	crossmingw32ce-binutils >= 2.15.91.0.2-2
BuildRequires:	flex
BuildRequires:	rpmbuild(macros) >= 1.315
%if %{with bootstrap}
# download rpm from http://cegcc.sourceforge.net/
BuildRequires:	cegcc
%else
BuildRequires:	crossmingw32ce-runtime >= 3.5
BuildRequires:	crossmingw32ce-w32api >= 3.1
%endif
Requires:	crossmingw32ce-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		arm-wince-mingw32ce
%define		target_platform	arm-wince-mingw32ce
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{gccarch}/%{version}

%define		_noautostrip	.*/lib.*\\.a

# -march=i686 is invalid
# so as i can't decide whether to use -march=armv4 or -march=armv5, i'll just strip
%define		filterout_c		-march=.*
%define		filterout_cxx	-march=.*

%description
crossmingw32ce is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32CE build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32ce, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l de.UTF-8
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Win32 zu generieren.

%description -l pl.UTF-8
crossmingw32ce jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek Mingw32CE. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32ce,
oraz z bibliotek w formacie COFF.

Ten pakiet zawiera gcc generujące skrośnie kod dla Win32.

%package c++
Summary:	Mingw32CE binary utility development utilities - g++
Summary(pl.UTF-8):	Zestaw narzędzi mingw32ce - g++
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description c++
crossmingw32ce is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32CE build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32ce, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl.UTF-8
crossmingw32ce jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32ce. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32ce,
oraz z bibliotek w formacie COFF.

Ten pakiet zawiera g++ generujące kod pod Win32 oraz bibliotekę
libstdc++.

%prep
%setup -q -n gcc
%if %{with bootstrap}
install -d winsup/w32api
ln -s /usr/ppc/%{target}/include/w32api winsup/w32api/include
%endif
#{!?debug:%patch0 -p1}
%patch1 -p0

%build
%if %{with bootstrap}
#for tool in as ar dlltool ld nm ranlib strip; do
#	ln -sf %{arch}/bin/$tool winsup/bin/$tool
#done
build_tooldir=`pwd`/winsup
includedir=/usr/ppc/%{target}/include
%else
build_tooldir=%{arch}
includedir=/usr/%{target}/include
%endif

cp /usr/share/automake/config.sub .
cp /usr/share/automake/config.sub boehm-gc

rm -rf obj-%{target_platform}
install -d obj-%{target_platform}
cd obj-%{target_platform}

# note: alpha's -mieee and sparc's -mtune=* are not valid for target's g++
CFLAGS="%{rpmcflags}" \
%ifarch alpha
CXXFLAGS="`echo '%{rpmcflags}' | sed -e 's/ \?-mieee\>//'`" \
%else
%ifarch sparc sparc64 sparcv9
CXXFLAGS="`echo '%{rpmcflags}' | sed -e 's/ \?-mtune[=0-9a-z]*//'`" \
%else
CXXFLAGS="%{rpmcflags}" \
%endif
%endif
LDFLAGS="%{rpmldflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--bindir=%{arch}/bin \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--includedir=$includedir \
	--disable-shared \
	--enable-threads \
	--enable-languages="c,c++" \
	--enable-c99 \
	--enable-long-long \
	--disable-nls \
	--with-gnu-as \
	--with-gnu-ld \
	--with-mangler-in-ld \
	--with-gxx-include-dir=%{arch}/include/g++ \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=%{target}

%{__make} all

# spec files for msvcrt*.dll configurations
cd gcc
for n in msvcrt msvcrt20 msvcrt40; do
	sed "s/crtdll/$n/g" <specs | sed "s/crt1/crt2/g" >specs.$n
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

cd obj-%{target_platform}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd gcc
install specs.msvcrt specs.msvcrt20 specs.msvcrt40 $RPM_BUILD_ROOT%{gcclib}
cd ../..

mv -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-* $RPM_BUILD_ROOT%{_bindir}

# already in arch/lib, shouldn't be here
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$RPM_BUILD_ROOT%{gcclib}
mkdir	$gccdir/tmp
# we have to save these however
mv -f	$gccdir/include/syslimits.h $gccdir/tmp
rm -rf	$gccdir/include
mv -f	$gccdir/tmp $gccdir/include
cp -f	$gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf	$gccdir/install-tools

%if 0%{!?debug:1}
%{target}-strip -g -R.note -R.comment $RPM_BUILD_ROOT%{gcclib}/libgcc.a
%{target}-strip -g -R.note -R.comment $RPM_BUILD_ROOT%{gcclib}/libgcov.a
%{target}-strip -g -R.note -R.comment $RPM_BUILD_ROOT%{arch}/lib/lib*.a
%endif

# restore hardlinks
ln -f $RPM_BUILD_ROOT%{_bindir}/%{target}-{g++,c++}
ln -f $RPM_BUILD_ROOT%{arch}/bin/{g++,c++}

# the same... make hardlink
ln -f $RPM_BUILD_ROOT%{arch}/bin/gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc*
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{arch}/bin/gcc
%{arch}/lib/libiberty.a

%dir %{gccarch}
%dir %{gcclib}
%attr(755,root,root) %{gcclib}/cc1
%attr(755,root,root) %{gcclib}/collect2
%{gcclib}/libgcc.a
%{gcclib}/libgcov.a
%{gcclib}/specs*
%{gcclib}/include

%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%{arch}/lib/libssp.a
%{arch}/lib/libssp.la
%{arch}/lib/libssp_nonshared.a
%{arch}/lib/libssp_nonshared.la

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-[cg]++
%attr(755,root,root) %{arch}/bin/[cg]++
%attr(755,root,root) %{gcclib}/cc1plus
%{arch}/lib/libstdc++.a
%{arch}/lib/libstdc++.la
%{arch}/lib/libsupc++.a
%{arch}/lib/libsupc++.la
%{arch}/include/g++
%{_mandir}/man1/%{target}-g++.1*
