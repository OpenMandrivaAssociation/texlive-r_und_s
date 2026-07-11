%global tl_name r_und_s
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3i
Release:	%{tl_revision}.1
Summary:	Chemical hazard codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/r_und_s
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/r_und_s.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/r_und_s.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The r_und_s package decodes the german 'R- und S-Satze', which are
numerically coded security advice for chemical substances into plain
text. This is, e.g., used to compose security sheets or lab protocols
and especially useful for students of chemistry. There are four
packages, giving texts in German, English, French and Dutch.

