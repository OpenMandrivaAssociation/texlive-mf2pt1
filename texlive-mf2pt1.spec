%define		texmfdistdir		%{_datadir}/texmf-dist

Name:		texlive-mf2pt1
Version:	20111028
Release:	1
Summary:	Produce PostScript Type 1 fonts from Metafont source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/mf2pt1
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.doc.tar.xz
BuildArch:	noarch

%post
%{_bindir}/mktexlsr %{_datadir}/texmf-dist

%postun
if [ $1 -eq 0 ]; then
    %{_bindir}/mktexlsr %{_datadir}/texmf-dist
fi

%description
mf2pt1 facilitates producing PostScript Type 1 fonts from a Metafont
source file.  mf2pt1's advantage over tools such as TeXtrace and
mftrace is that it does not rely on bitmap tracing and therefore can
produce higher-quality Type 1 fonts than trace-based tools.  The catch
is that mf2pt1 imposes a number of restrictions on the Metafont input
so it is not, as the name may imply, an automatic converter of
arbitrary Metafont fonts to Type 1 format.

%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}

mkdir -p %{buildroot}%{_infodir}
install -m644 texmf/doc/info/mf2pt1.info %{buildroot}%{_infodir}

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{texmfdistdir}/scripts/mf2pt1/mf2pt1.pl mf2pt1
popd

%files
%{_bindir}/mf2pt1
%{texmfdistdir}/scripts/mf2pt1
%{texmfdistdir}/metapost/mf2pt1
%doc %{_infodir}/mf2pt1.info*
%doc %{texmfdistdir}/doc/support/mf2pt1
