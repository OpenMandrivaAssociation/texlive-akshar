%global tl_name akshar
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Support for syllables in the Devanagari script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/akshar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akshar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX3 package provides macros and interfaces to work with
Devanagari characters and syllables in a more correct way.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/akshar
%dir %{_datadir}/texmf-dist/source/latex/akshar
%dir %{_datadir}/texmf-dist/tex/latex/akshar
%doc %{_datadir}/texmf-dist/doc/latex/akshar/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/akshar/akshar.pdf
%doc %{_datadir}/texmf-dist/source/latex/akshar/HackNF_B.ttf
%doc %{_datadir}/texmf-dist/source/latex/akshar/HackNF_BI.ttf
%doc %{_datadir}/texmf-dist/source/latex/akshar/HackNF_I.ttf
%doc %{_datadir}/texmf-dist/source/latex/akshar/HackNF_R.ttf
%doc %{_datadir}/texmf-dist/source/latex/akshar/akshar.dtx
%doc %{_datadir}/texmf-dist/source/latex/akshar/akshar.ins
%doc %{_datadir}/texmf-dist/source/latex/akshar/siddhanta.ttf
%{_datadir}/texmf-dist/tex/latex/akshar/akshar.sty
