import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')

BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')
BACKUP = False

SITE_ROOT = "/"
SITE_WWW_URL = "http://www.yoursite.com"
SITE_NAME = "Your Site"
SITE_AUTHOR = "Your Name"
SITE_ROOT = "/"

#Url Configuration
GENERATE_ABSOLUTE_FS_URLS = False

# Clean urls causes Hyde to generate urls without extensions. Examples:
# http://example.com/section/page.html becomes
# http://example.com/section/page/, and the listing for that section becomes
# http://example.com/section/
# The built-in CherryPy webserver is capable of serving pages with clean urls
# without any additional configuration, but Apache will need to use Mod_Rewrite
# to map the clean urls to the actual html files.  The HtaccessGenerator site
# post processor is capable of automatically generating the necessary
# RewriteRules for use with Apache.
GENERATE_CLEAN_URLS = False

# A list of filenames (without extensions) that will be considered listing
# pages for their enclosing folders.
# LISTING_PAGE_NAMES = ['index']
LISTING_PAGE_NAMES = ['listing', 'index', 'default']

# Determines whether or not to append a trailing slash to generated urls when
# clean urls are enabled.
APPEND_SLASH = False

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# should be specified. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.

MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',),
        '.ccss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CleverCSS',
                'hydeengine.media_processors.YUICompressor',),
        '.sass':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.SASS',
                'hydeengine.media_processors.YUICompressor',),                
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.YUICompressor',),                
        '.hss':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.HSS',
                'hydeengine.media_processors.YUICompressor',),
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',)
    } 
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' : 
            ('hydeengine.content_processors.PassthroughProcessor',)
            }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

class CassandraDef(object):
    stable_version = '0.6.3'
    stable_release_date = '2010-06-29'
    devel_version = '0.6.0-rc1'
    devel_release_date = '2010-03-31'
    devel_exists = False
    _apache_base_url = 'http://www.apache.org'
    _svn_base_url = 'https://svn.apache.org/repos/asf'
    _apache_path = 'cassandra'
    _archive_prefix = 'apache-cassandra'
  
    @classmethod 
    def keys_url(cls):
        return "%s/dist/%s/KEYS" % (cls._apache_base_url, cls._apache_path)
 
    @classmethod 
    def binary_filename(cls, version=stable_version):
        return "%s-%s-bin.tar.gz" % (cls._archive_prefix, version)

    @classmethod 
    def binary_path(cls, version):
	base_version = version.split('-')[0]
        return "%s/%s/%s" % \
            (cls._apache_path, base_version, cls.binary_filename(version))

    @classmethod 
    def binary_url(cls, version=stable_version):
        return "%s/dyn/closer.cgi?path=/%s"  % \
                (cls._apache_base_url, cls.binary_path(version))

    @classmethod 
    def binary_artifacts_url(cls, version=stable_version):
        return "%s/dist/%s" % (cls._apache_base_url, cls.binary_path(version))

    @classmethod 
    def source_filename(cls, version=stable_version):
        return "%s-%s-src.tar.gz" % (cls._archive_prefix, version)

    @classmethod 
    def source_path(cls, version):
	base_version = version.split('-')[0]
        return "%s/%s/%s" % \
            (cls._apache_path, base_version, cls.source_filename(version))

    @classmethod 
    def source_url(cls, version=stable_version):
        return "%s/dyn/closer.cgi?path=/%s"  % \
                (cls._apache_base_url, cls.source_path(version))

    @classmethod 
    def source_artifacts_url(cls, version=stable_version):
        return "%s/dist/%s" % (cls._apache_base_url, cls.source_path(version))

    @classmethod 
    def changelog(cls):
        return "%s/%s/tags/cassandra-%s/CHANGES.txt" % \
                (cls._svn_base_url, cls._apache_path, cls.stable_version)

    @classmethod 
    def subversion_url(cls):
        return "%s/%s" % (cls._svn_base_url, cls._apache_path)

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS,
    'cassandra_stable': CassandraDef.stable_version,
    'cassandra_stable_release_date': CassandraDef.stable_release_date,
    'cassandra_devel': CassandraDef.devel_version,
    'cassandra_devel_release_date': CassandraDef.devel_release_date,
    'subversion_url': CassandraDef.subversion_url(),
    'changelog': CassandraDef.changelog(),
    'binary_filename': CassandraDef.binary_filename(),
    'binary_download': CassandraDef.binary_url(),
    'source_filename': CassandraDef.source_filename(),
    'source_download': CassandraDef.source_url(),
    'devbin_filename': CassandraDef.binary_filename(CassandraDef.devel_version),
    'devbin_download': CassandraDef.binary_url(CassandraDef.devel_version),
    'devsrc_filename': CassandraDef.source_filename(CassandraDef.devel_version),
    'devsrc_download': CassandraDef.source_url(CassandraDef.devel_version),
    'keys_url': CassandraDef.keys_url(),
    'binary_artifacts_url': CassandraDef.binary_artifacts_url(),
    'source_artifacts_url': CassandraDef.source_artifacts_url(),
    'devel_binary_artifacts_url': CassandraDef.binary_artifacts_url(
            CassandraDef.devel_version),
    'devel_source_artifacts_url': CassandraDef.source_artifacts_url(
            CassandraDef.devel_version),
    'devel_exists': CassandraDef.devel_exists,
}

FILTER = { 
    'include': (".htaccess",),
    'exclude': (".*","*~")
}        


#Processor Configuration 

# 
#  Set this to the output of `which growlnotify`. If `which`  returns emtpy,
#  install growlnotify from the Extras package that comes with the Growl disk image.
# 
#
GROWL = None

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
YUI_COMPRESSOR = "./lib/yuicompressor-2.4.1.jar"
#YUI_COMPRESSOR = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS

#Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)
