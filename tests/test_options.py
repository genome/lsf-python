from lsf import options
from pythonlsf import lsf as api
import mock
import unittest


class OptionTest(unittest.TestCase):
    def mock_request(self):
        request = mock.Mock()
        request.options = 0
        request.options2 = 0
        request.options3 = 0

        return request

    def test_flag_group_1(self):
        test_options = {
            'errFile': api.SUB_ERR_FILE,
            'inFile': api.SUB_IN_FILE,
            'jobName': api.SUB_JOB_NAME,
            'mail_user': api.SUB_MAIL_USER,
            'outFile': api.SUB_OUT_FILE,
            'projectName': api.SUB_PROJECT_NAME,
            'queue': api.SUB_QUEUE,
        }

        for name, flag in test_options.iteritems():
            request = self.mock_request()
            options.set_options(request, {name: 'test_value'})
            self.assertEqual(request.options, flag)
            self.assertEqual(getattr(request, name), 'test_value')

    def test_flag_group_2(self):
        test_options = {
            'group': api.SUB2_JOB_GROUP,
        }

        for name, flag in test_options.iteritems():
            request = self.mock_request()
            options.set_options(request, {name: 'test_value'})
            self.assertEqual(request.options2, flag)
            self.assertEqual(getattr(request, name), 'test_value')

    def test_begin_term_times(self):
        request = self.mock_request()

        options.set_options(request, {'beginTime': '123', 'termTime': '456'})
        self.assertEqual(request.beginTime, 123)
        self.assertEqual(request.termTime, 456)

    def test_processors(self):
        request = self.mock_request()

        options.set_options(request,
                {'numProcessors': 4, 'maxNumProcessors': 6})
        self.assertEqual(request.numProcessors, 4)
        self.assertEqual(request.maxNumProcessors, 6)
