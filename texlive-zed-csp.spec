# revision 17258
# category Package
# catalog-ctan /macros/latex/contrib/zed-csp
# catalog-date 2008-04-05 21:05:50 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-zed-csp
Version:	20080405
Release:	5
Summary:	Typesetting Z and CSP format specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zed-csp
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080405-2
+ Revision: 757781
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080405-1
+ Revision: 719972
- texlive-zed-csp
- texlive-zed-csp
- texlive-zed-csp

