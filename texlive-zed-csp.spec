%global tl_name zed-csp
%global tl_revision 17258

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesetting Z and CSP format specifications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zed-csp
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zed-csp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports real-time CSP and incorporates the functionality of
Spivey's original Z package, written for LaTeX 2.09.

