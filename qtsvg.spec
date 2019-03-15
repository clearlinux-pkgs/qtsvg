#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtsvg
Version  : 5.12.2
Release  : 14
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.2/submodules/qtsvg-everywhere-src-5.12.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.2/submodules/qtsvg-everywhere-src-5.12.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: qtsvg-lib = %{version}-%{release}
Requires: qtsvg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
This directory contains autotests and benchmarks based on QTestlib. In order
to run the autotests reliably, you need to configure a desktop to match the
test environment that these tests are written for.

%package dev
Summary: dev components for the qtsvg package.
Group: Development
Requires: qtsvg-lib = %{version}-%{release}
Provides: qtsvg-devel = %{version}-%{release}

%description dev
dev components for the qtsvg package.


%package lib
Summary: lib components for the qtsvg package.
Group: Libraries
Requires: qtsvg-license = %{version}-%{release}

%description lib
lib components for the qtsvg package.


%package license
Summary: license components for the qtsvg package.
Group: Default

%description license
license components for the qtsvg package.


%prep
%setup -q -n qtsvg-everywhere-src-5.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1552682228
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtsvg
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.GPL3-EXCEPT
cp LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.GPLv3
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.LGPL3
cp LICENSE.LGPLv21 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.LGPLv21
cp LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/LICENSE.LGPLv3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvgfont_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvggraphics_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvghandler_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvgnode_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvgstructure_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvgstyle_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qsvgtinydocument_p.h
/usr/include/qt5/QtSvg/5.12.2/QtSvg/private/qtsvgglobal_p.h
/usr/include/qt5/QtSvg/QGraphicsSvgItem
/usr/include/qt5/QtSvg/QSvgGenerator
/usr/include/qt5/QtSvg/QSvgRenderer
/usr/include/qt5/QtSvg/QSvgWidget
/usr/include/qt5/QtSvg/QtSvg
/usr/include/qt5/QtSvg/QtSvgDepends
/usr/include/qt5/QtSvg/QtSvgVersion
/usr/include/qt5/QtSvg/qgraphicssvgitem.h
/usr/include/qt5/QtSvg/qsvggenerator.h
/usr/include/qt5/QtSvg/qsvgrenderer.h
/usr/include/qt5/QtSvg/qsvgwidget.h
/usr/include/qt5/QtSvg/qtsvgglobal.h
/usr/include/qt5/QtSvg/qtsvgversion.h
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfig.cmake
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfigVersion.cmake
/usr/lib64/cmake/Qt5Svg/Qt5Svg_QSvgIconPlugin.cmake
/usr/lib64/cmake/Qt5Svg/Qt5Svg_QSvgPlugin.cmake
/usr/lib64/libQt5Svg.prl
/usr/lib64/libQt5Svg.so
/usr/lib64/pkgconfig/Qt5Svg.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Svg.so.5
/usr/lib64/libQt5Svg.so.5.12
/usr/lib64/libQt5Svg.so.5.12.2
/usr/lib64/qt5/plugins/iconengines/libqsvgicon.so
/usr/lib64/qt5/plugins/imageformats/libqsvg.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtsvg/LICENSE.FDL
/usr/share/package-licenses/qtsvg/LICENSE.GPL2
/usr/share/package-licenses/qtsvg/LICENSE.GPL3
/usr/share/package-licenses/qtsvg/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtsvg/LICENSE.GPLv3
/usr/share/package-licenses/qtsvg/LICENSE.LGPL3
/usr/share/package-licenses/qtsvg/LICENSE.LGPLv21
/usr/share/package-licenses/qtsvg/LICENSE.LGPLv3
