import os
import sys
from xlnoserunner import LocalEZSetup

local_ez_setup = LocalEZSetup(os.getcwdu())
nose = local_ez_setup.ensure_module('nose')

# Run Tests!
test_suite = sys.argv[1]
build_dir = sys.argv[2]

xml_file = os.path.join(build_dir, 'nosetests.xml')

success = nose.run(argv=['nosetests', '-v', test_suite, '--with-xunit', '--xunit-file=%s' % xml_file])
if not success:
    sys.exit(1)