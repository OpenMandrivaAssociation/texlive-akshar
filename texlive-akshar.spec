Name:		texlive-akshar
Version:	56277
Release:	2
Summary:	Support for syllables in the Devanagari script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/akshar
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX3 package provides macros and interfaces to work with
Devanagari characters and syllables in a more correct way.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/akshar
%{_texmfdistdir}/tex/latex/akshar
%doc %{_texmfdistdir}/doc/latex/akshar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
