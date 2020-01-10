Name:           maven-project-info-reports-plugin
Version:        2.6
Release:        8%{?dist}
Summary:        Maven Project Info Reports Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-project-info-reports-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: apache-commons-parent
BuildRequires: maven-local
BuildRequires: maven-dependency-tree
BuildRequires: maven-plugin-annotations
BuildRequires: maven-plugin-plugin
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-doxia-tools
BuildRequires: maven-shared-jar
BuildRequires: maven-wagon
BuildRequires: maven-scm
BuildRequires: maven-doxia-sink-api
BuildRequires: maven-doxia-logging-api
BuildRequires: maven-doxia-core
BuildRequires: maven-doxia-module-xhtml
BuildRequires: maven-doxia-sitetools
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-component-api
BuildRequires: plexus-i18n
BuildRequires: plexus-utils
BuildRequires: apache-commons-validator
BuildRequires: httpunit
BuildRequires: maven-plugin-testing-harness
BuildRequires: servlet3
BuildRequires: maven-jarsigner-plugin
BuildRequires: keytool-maven-plugin
BuildRequires: joda-time
BuildRequires: maven-resources-plugin

Obsoletes: maven2-plugin-project-info-reports <= 0:2.0.8
Provides: maven2-plugin-project-info-reports = 0:%{version}-%{release}

%description
The Maven Project Info Reports Plugin is a plugin 
that generates standard reports for the specified project.
  

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -c
pushd %{name}-%{version}
# removed cvsjava provider since we don't support it anymore
%pom_remove_dep :maven-scm-provider-cvsjava
%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"
popd

%build
pushd %{name}-%{version}
%mvn_build -f
popd

%install
pushd %{name}-%{version}
%mvn_install
popd

%files -f %{name}-%{version}/.mfiles
%dir %{_javadir}/%{name}
%doc %{name}-%{version}/LICENSE %{name}-%{version}/NOTICE

%files javadoc -f %{name}-%{version}/.mfiles-javadoc
%doc %{name}-%{version}/LICENSE %{name}-%{version}/NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.6-8
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 2.6-7
- Migrate away from mvn-rpmbuild (Resolves: #997511)
- Add missing BR: maven-resources-plugin

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-5
- Remove dependencies with test scope

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-4
- Add missing Requires on doxia packages
- Resolves: rhbz#909250

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 2.6-3
- Migrate from maven-doxia to doxia subpackages (Resolves: #909250)
- Add BR on maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 2.6-2
- Migrated to plexus-containers-container-default (Resolves: #878559)
- Removed build dependency on netbeans-cvsclient

* Mon Oct 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Tue Sep 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-6
- Remove cvsjava support (still can use cvsexe)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-4
- One more missing R - joda-time.

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-3
- Requires maven-scm.

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-2
- Add missing R.

* Mon May 30 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-1
- Update to upstream version 2.4.

* Mon May 23 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- UPdate to upstream version 2.3.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 2.2-5
- Removed obsolete patch
- tomcat5 -> tomcat6 BRs/Rs

* Tue Oct 26 2010 akurtakov <akurtakov@redhat.com> 2.2-4
- Fix apache-commons-validator BR/R.

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Add missing BR netbeans-cvsclient

* Mon Jun 07 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Added missing requires

* Thu Jun 02 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package
