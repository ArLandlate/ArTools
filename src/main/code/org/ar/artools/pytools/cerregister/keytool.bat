cd /D %JAVA_HOME%/jre/lib/security/

keytool -import -alias %1 -keystore %1 -file %2