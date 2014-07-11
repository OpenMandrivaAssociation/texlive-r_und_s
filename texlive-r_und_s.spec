# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/r_und_s
# catalog-date 2008-08-24 22:21:06 +0200
# catalog-license other-free
# catalog-version 1.3i
Name:		texlive-r_und_s
Version:	1.3i
Release:	8
Summary:	Chemical hazard codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/r_und_s
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/r_und_s.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/r_und_s.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The r_und_s package decodes the german 'R- und S-Satze', which
are numerically coded security advice for chemical substances
into plain text. This is, e.g., used to compose security sheets
or lab protocols and especially useful for students of
chemistry. There are four packages, giving texts in German,
English, French and Dutch.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/r_und_s/eng_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/eng_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/fr_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/fr_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/nl_rs.sty
%{_texmfdistdir}/tex/latex/r_und_s/nl_rs.tex
%{_texmfdistdir}/tex/latex/r_und_s/r_und_s.sty
%{_texmfdistdir}/tex/latex/r_und_s/r_und_s.tex
%doc %{_texmfdistdir}/doc/latex/r_und_s/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3i-2
+ Revision: 755781
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3i-1
+ Revision: 719472
- texlive-r_und_s
- texlive-r_und_s
- texlive-r_und_s
- texlive-r_und_s

