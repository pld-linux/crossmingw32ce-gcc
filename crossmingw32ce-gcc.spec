#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingw)
#
Summary:	Cross Mingw32 GNU binary utility development utilities - gcc
Summary(es):	Utilitarios para desarrollo de binarios de la GNU - Mingw32 gcc
Summary(fr):	Utilitaires de développement binaire de GNU - Mingw32 gcc
Summary(pl):	Skro¶ne narzêdzia programistyczne GNU dla Mingw32 - gcc
Summary(pt_BR): Utilitários para desenvolvimento de binários da GNU - Mingw32 gcc
Summary(tr):	GNU geliþtirme araçlarý - Mingw32 gcc
Name:		crossmingw32ce-gcc
Version:	4.1.1
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	ad9f97a4d04982ccf4fd67cb464879f3
%define		apiver	3.7
Source1:	http://dl.sourceforge.net/mingw/w32api-%{apiver}.tar.gz
# Source1-md5:	0b3a6d08136581c93b3a3207588acea9
%define		runver	3.10
Source2:	http://dl.sourceforge.net/mingw/mingw-runtime-%{runver}.tar.gz
# Source2-md5:	7fa2638d23136fd84d5d627bef3b408a
Patch0:		gcc-nodebug.patch
Patch1:		crossmingw32-gcc-noioctl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	crossmingw32ce-binutils >= 2.15.91.0.2-2
BuildRequires:	flex
%if !%{with bootstrap}
BuildRequires:	crossmingw32ce-runtime >= 3.5
BuildRequires:	crossmingw32ce-w32api >= 3.1
%endif
BuildRequires:	mpfr-devel
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32ce
%define		target_platform i386-pc-mingw32ce
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{gccarch}/%{version}

%define		_noautostrip	.*/lib.*\\.a	

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l de
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Win32 zu generieren.

%description -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek Mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera gcc generuj±ce skro¶nie kod dla Win32.

%package c++
Summary:	Mingw32 binary utility development utilities - g++
Summary(pl):	Zestaw narzêdzi mingw32 - g++
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera g++ generuj±ce kod pod Win32 oraz bibliotekê
libstdc++.

# does this even work?
%package objc
Summary:	Mingw32 binary utility development utilities - objc
Summary(pl):	Zestaw narzêdzi mingw32 - objc
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc compiler.

%description objc -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator objc generuj±cy kod pod Win32.

# does this even work?
%package fortran
Summary:	Mingw32 binary utility development utilities - Fortran
Summary(pl):	Zestaw narzêdzi mingw32 - Fortran
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description fortran
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Fortran compiler.

%description fortran -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Fortranu generuj±cy kod pod Win32.

# does this even work?
%package java
Summary:	Mingw32 binary utility development utilities - Java
Summary(pl):	Zestaw narzêdzi mingw32 - Java
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Java compiler.

%description java -l pl

crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Javy generuj±cy kod pod Win32.

%prep
%setup -q -n gcc-%{version}
%if %{with bootstrap}
mkdir winsup
tar xzf %{SOURCE1} -C winsup
tar xzf %{SOURCE2} -C winsup
%endif
#{!?debug:%patch0 -p1}
%patch1 -p1

%build
%if %{with bootstrap}
for tool in as ar dlltool ld nm ranlib strip ; do
	ln -sf %{arch}/bin/$tool winsup/bin/$tool
done
build_tooldir=`pwd`/winsup
%else
build_tooldir=%{arch}
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
	--includedir=%{arch}/include \
	--disable-shared \
	--enable-threads \
	--enable-languages="c,c++,fortran,java,objc" \
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

%files objc
%defattr(644,root,root,755)
%attr(755,root,root) %{gcclib}/cc1obj
%{arch}/lib/libobjc.a
%{arch}/lib/libobjc.la

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gfortran
%attr(755,root,root) %{arch}/bin/gfortran
%attr(755,root,root) %{gcclib}/f951
%{arch}/lib/libgfortran.a
%{arch}/lib/libgfortran.la
%{arch}/lib/libgfortranbegin.a
%{arch}/lib/libgfortranbegin.la
%{_mandir}/man1/%{target}-gfortran.1*

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcj
%attr(755,root,root) %{_bindir}/%{target}-gcjh
%attr(755,root,root) %{_bindir}/%{target}-gjnih
%attr(755,root,root) %{_bindir}/%{target}-grepjar
%attr(755,root,root) %{_bindir}/%{target}-fastjar
%attr(755,root,root) %{_bindir}/%{target}-jcf-dump
%attr(755,root,root) %{_bindir}/%{target}-jv-scan
#%attr(755,root,root) %{arch}/bin/grepjar
#%attr(755,root,root) %{arch}/bin/jar
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
%{_mandir}/man1/%{target}-gcj.1*
%{_mandir}/man1/%{target}-gcjh.1*
%{_mandir}/man1/%{target}-gjnih.1*
%{_mandir}/man1/%{target}-grepjar.1*
%{_mandir}/man1/%{target}-fastjar.1*
%{_mandir}/man1/%{target}-jcf-dump.1*
%{_mandir}/man1/%{target}-jv-scan.1*
