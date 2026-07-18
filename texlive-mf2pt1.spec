%global tl_name mf2pt1
%global tl_revision 71883
%global tl_bin_links mf2pt1:%{_texmfdistdir}/scripts/mf2pt1/mf2pt1.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.8
Release:	%{tl_revision}.1
Summary:	Convert stylized Metafont to PostScript Type 1
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/mf2pt1
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mf2pt1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mf2pt1.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
mf2pt1 is a Perl script that facilitates producing PostScript Type 1
fonts from a Metafont source file. It is not, as the name may imply, an
automatic converter of arbitrary Metafont fonts to Type 1 format. mf2pt1
imposes a number of restrictions on the Metafont input. If these
restrictions are met, mf2pt1 will produce valid Type 1 output with more
accurate control points than can be reverse-engineered by TeXtrace,
mftrace, and other programs which convert bitmaps to outline fonts.

