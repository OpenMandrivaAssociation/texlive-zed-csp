# revision 17258
# category Package
# catalog-ctan /macros/latex/contrib/zed-csp
# catalog-date 2008-04-05 21:05:50 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-zed-csp
Version:	20080405
Release:	1
Summary:	Typesetting Z and CSP format specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zed-csp
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package supports real-time CSP and incorporates the
functionality of Spivey's original Z package, written for LaTeX
2.09.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zed-csp/zed-csp.sty
%doc %{_texmfdistdir}/doc/latex/zed-csp/csp2e.pdf
%doc %{_texmfdistdir}/doc/latex/zed-csp/csp2e.tex
%doc %{_texmfdistdir}/doc/latex/zed-csp/zed2e.pdf
%doc %{_texmfdistdir}/doc/latex/zed-csp/zed2e.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
