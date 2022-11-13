Name:		texlive-zed-csp
Version:	17258
Release:	1
Summary:	Typesetting Z and CSP format specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zed-csp
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports real-time CSP and incorporates the
functionality of Spivey's original Z package, written for LaTeX
2.09.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zed-csp/zed-csp.sty
%doc %{_texmfdistdir}/doc/latex/zed-csp/csp2e.pdf
%doc %{_texmfdistdir}/doc/latex/zed-csp/csp2e.tex
%doc %{_texmfdistdir}/doc/latex/zed-csp/zed2e.pdf
%doc %{_texmfdistdir}/doc/latex/zed-csp/zed2e.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
