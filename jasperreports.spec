%{?_javapackages_macros:%_javapackages_macros}
Name:          jasperreports
# the JR newest release requires
# xmlbeans >= 2.5.0
# castor-xml modules see also https://bugzilla.redhat.com/show_bug.cgi?id=820676
Version:       4.0.2
Release:       10.3
Summary:       Report-generating tool
Group:	       Development/Java
License:       LGPLv3+
URL:           http://jasperforge.org/projects/jasperreports/
# wget http://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%204.0.2/jasperreports-4.0.2-project.tar.gz
# tar xf jasperreports-4.0.2-project.tar.gz
# find jasperreports-4.0.2 -name '*.class' -delete
# find jasperreports-4.0.2 -name '*.jar' -delete
# rm -rf lib/*
# tar czf jasperreports-4.0.2-clean.tar.gz jasperreports-4.0.2
Source0:       %{name}-%{version}-clean.tar.gz
# remove groovy-all.jar references
Patch0:        %{name}-%{version}-use_system_asm.patch
# configure javaflow ant task
# build fix for commons-javaflow 1.0
Patch1:        %{name}-%{version}-configure_javaflow.patch
# exclude Barcode4J and Barbecue modules
Patch2:        %{name}-%{version}-exclude_barcode4j_and_barbecue.patch
# remove Xmx128m to javadoc task
Patch3:        %{name}-%{version}-no_maxmemory_for_javadoc.patch
# use commons-codec instead of unavailable (non free) W3C Base64 decode/encode
Patch4:        %{name}-%{version}-use_commons-codec.patch
# don't build -font.jar
Patch5:        %{name}-%{version}-disable_fonts.patch
# disable build of sampleref
Patch6:        %{name}-%{version}-disable_sampleref.patch

Patch7:        %{name}-%{version}-ecj4.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-javaflow
BuildRequires: apache-commons-logging
BuildRequires: apache-poi
BuildRequires: batik
BuildRequires: bcel
BuildRequires: bsh
BuildRequires: dom4j
BuildRequires: ecj >= 1:3.4.2-13
BuildRequires: geronimo-saaj
BuildRequires: groovy
BuildRequires: hibernate3
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hsqldb1
BuildRequires: itext-core
BuildRequires: jaxen
BuildRequires: jcommon
BuildRequires: jexcelapi
BuildRequires: jfreechart
BuildRequires: log4j12
BuildRequires: objectweb-asm3
BuildRequires: rhino
BuildRequires: springframework
BuildRequires: springframework-beans
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires:      apache-commons-beanutils
Requires:      apache-commons-codec
Requires:      apache-commons-collections
Requires:      apache-commons-digester
Requires:      apache-commons-javaflow
Requires:      apache-commons-logging
Requires:      batik
Requires:      bcel
Requires:      ecj >= 1:3.4.2-13
Requires:      geronimo-saaj
Requires:      hsqldb1
Requires:      itext-core
Requires:      jcommon
Requires:      jfreechart
Requires:      springframework
Requires:      springframework-beans
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch

%description
JasperReports is a powerful open source
report-generating tool that has the ability
to deliver rich content onto the screen, to
the printer or into PDF, HTML, XLS, CSV and
XML files. It is entirely written in Java
and can be used in a variety of Java enabled
applications, including J2EE or Web
Its main purpose is to help creating page
oriented, ready to print documents in a
simple and flexible manner.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%package manual
Summary:       Manual for %{name}

%description manual
Documentation for %{name}.

%prep
%setup -q
find . -name 'PieChartReport.bak' -delete
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0

sed -i 's/\r//' changes.txt

ln -sf $(build-classpath ant) lib/ant-1.7.1.jar
ln -sf $(build-classpath antlr) lib/antlr-2.7.5.jar
ln -sf $(build-classpath batik-all) lib/
ln -sf $(build-classpath bcel) lib/bcel-5.2.jar
ln -sf $(build-classpath bsh) lib/bsh-2.0b4.jar
ln -sf $(build-classpath commons-beanutils) lib/commons-beanutils-1.8.0.jar
ln -sf $(build-classpath commons-codec) lib/
ln -sf $(build-classpath commons-collections) lib/commons-collections-2.1.1.jar
ln -sf $(build-classpath commons-digester) lib/commons-digester-1.7.jar
ln -sf $(build-classpath commons-javaflow) lib/commons-javaflow-20060411.jar
ln -sf $(build-classpath commons-logging) lib/commons-logging-1.0.4.jar
ln -sf $(build-classpath dom4j) lib/dom4j-1.6.1.jar
ln -sf $(build-classpath ecj) lib/jdt-compiler-3.1.1.jar
ln -sf $(build-classpath hibernate3/hibernate-core-3) lib/hibernate3.jar
ln -sf $(build-classpath hibernate-jpa-2.0-api) lib/jpa.jar
ln -sf $(build-classpath springframework/spring-beans) lib/spring-beans-2.5.5.jar
ln -sf $(build-classpath springframework/spring-core) lib/spring-core-2.5.5.jar
ln -sf $(build-classpath groovy) lib/groovy-all-1.7.5.jar
ln -sf $(build-classpath hsqldb1-1) lib/hsqldb-1.8.0-10.jar
ln -sf $(build-classpath itext) lib/iText-2.1.7.jar
ln -sf $(build-classpath jaxen) lib/jaxen-1.1.1.jar
ln -sf $(build-classpath jcommon) lib/jcommon-1.0.15.jar
ln -sf $(build-classpath jfreechart/jfreechart) lib/jfreechart-1.0.12.jar
ln -sf $(build-classpath jxl) lib/jxl-2.6.10.jar
ln -sf $(build-classpath log4j12-1.2.17) lib/log4j-1.2.15.jar
ln -sf $(build-classpath objectweb-asm3/asm) lib/
ln -sf $(build-classpath poi/apache-poi) lib/poi-3.6.jar
ln -sf $(build-classpath rhino) lib/rhino-1.7R1.jar
ln -sf $(build-classpath geronimo-saaj) lib/saaj-api-1.3.jar
ln -sf $(build-classpath tomcat-servlet-3.0-api) lib/servlet.jar
ln -sf $(build-classpath xalan-j2) lib/xalan-2.7.1.jar
ln -sf $(build-classpath xalan-j2-serializer) lib/serializer.jar
ln -sf $(build-classpath xerces-j2) lib/xercesImpl-2.7.0.jar
ln -sf $(build-classpath xml-commons-apis) lib/xml-apis.jar
ln -sf $(build-classpath xml-commons-apis-ext) lib/xml-apis-ext.jar

# remove. cause: unwanted
rm -rf src/org/w3c/tools/codec/Base64*

# remove. cause: unavailable build deps
rm -rf src/net/sf/jasperreports/data/mondrian/* \
  src/net/sf/jasperreports/olap/* \
  src/net/sf/jasperreports/components/barcode4j/* \
  src/net/sf/jasperreports/components/barbecue/*

sed -i 's|deprecation="true"|deprecation="false"|' build.xml

%pom_remove_dep net.sf.barcode4j:barcode4j
%pom_remove_dep net.sourceforge.barbecue:barbecue
%pom_remove_dep mondrian:mondrian
%pom_remove_dep com.keypoint:png-encoder

%pom_add_dep commons-codec:commons-codec::compile

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'bsh']/pom:groupId" bsh
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'bsh']/pom:version" 1.3.0

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'eclipse']/pom:groupId" org.eclipse.jdt
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jdtcore']/pom:artifactId" core

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:version" 1.8.9

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jcommon']/pom:groupId" org.jfree
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jfreechart']/pom:groupId" org.jfree

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']/pom:artifactId" hibernate-core
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']/pom:version" 3

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'commons-javaflow']/pom:groupId" org.apache.commons

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.persistence']/pom:groupId" org.hibernate.javax.persistence
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'persistence-api']/pom:artifactId" hibernate-jpa-2.0-api

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.xml.soap']/pom:groupId" org.apache.geronimo.specs
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'saaj-api']/pom:artifactId" geronimo-saaj_1.3_spec

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'rhino']/pom:groupId" org.mozilla
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'js']/pom:artifactId" rhino

%build

# DO NOT USE maven for build
%ant jar docs

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -m 644 dist/%{name}-applet-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-applet.jar
install -m 644 dist/%{name}-javaflow-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-javaflow.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar -a "%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
rm -rf dist/docs/api

%files -f .mfiles
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-applet.jar
%{_javadir}/%{name}/%{name}-javaflow.jar
%doc *.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%files manual
%doc dist/docs/*
%doc license.txt

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 4.0.2-9
- Use Requires: java-headless rebuild (#1067528)

* Fri Nov 15 2013 gil cattaneo <puntogil@libero.it> 4.0.2-8
- use hsqldb1

* Fri Nov 15 2013 gil cattaneo <puntogil@libero.it> 4.0.2-7
- use objectweb-asm3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 gil cattaneo <puntogil@libero.it> 4.0.2-4
- fix build for new ecj
- fix Build/Requires (iText >> itext-core; hibernate3 for f18 or major)
- used pom macros

* Tue Jul 17 2012 gil cattaneo <puntogil@libero.it> 4.0.2-3
- fix commmons-codec and jcommons gId in PATCH7

* Mon Jul 09 2012 gil cattaneo <puntogil@libero.it> 4.0.2-2
- fix license tag
- repackaged source0

* Wed May 09 2012 gil cattaneo <puntogil@libero.it> 4.0.2-1
- initial rpm

