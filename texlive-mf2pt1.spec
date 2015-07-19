# revision 33802
# category Package
# catalog-ctan /support/mf2pt1
# catalog-date 2014-05-02 06:53:00 +0200
# catalog-license lppl
# catalog-version 2.5a
Name:		texlive-mf2pt1
Epoch:		1
Version:	2.5a
Release:	4
Summary:	Produce PostScript Type 1 fonts from Metafont source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/mf2pt1
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-mf2pt1.bin = %{EVRD}

%description
mf2pt1 facilitates producing PostScript Type 1 fonts from a
Metafont source file. It is not, as the name may imply, an
automatic converter of arbitrary Metafont fonts to Type 1
format. mf2pt1 imposes a number of restrictions on the Metafont
input. If these restrictions are met, mf2pt1 will produce valid
Type 1 output with more accurate control points than can be
reverse-engineered by TeXtrace, mftrace, and other programs
which convert bitmaps to outline fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mf2pt1
%{_texmfdistdir}/metapost/mf2pt1/mf2pt1.mp
%{_texmfdistdir}/scripts/mf2pt1/mf2pt1.pl
%doc %{_infodir}/mf2pt1.info*
%doc %{_texmfdistdir}/doc/support/mf2pt1/ChangeLog
%doc %{_texmfdistdir}/doc/support/mf2pt1/README
%doc %{_texmfdistdir}/doc/support/mf2pt1/mf2pt1.pdf
%doc %{_texmfdistdir}/doc/support/mf2pt1/mf2pt1.texi

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/mf2pt1/mf2pt1.pl mf2pt1
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
