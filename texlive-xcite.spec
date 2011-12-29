# revision 23783
# category Package
# catalog-ctan /macros/latex/contrib/xcite
# catalog-date 2011-09-03 01:03:37 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-xcite
Version:	1.0
Release:	1
Summary:	Use citation keys from a different document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcite
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcite.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcite.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package lets you use citation keys from another document,
just as the xr package allows cross-document use of labels.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xcite/xcite.sty
%doc %{_texmfdistdir}/doc/latex/xcite/README
%doc %{_texmfdistdir}/doc/latex/xcite/xcite.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xcite/xcite.dtx
%doc %{_texmfdistdir}/source/latex/xcite/xcite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
