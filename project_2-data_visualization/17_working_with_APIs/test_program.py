import unittest

import python_repos_revised as pr


class PythonReposTestCase(unittest.TestCase):
    """Tests for python_repos_revised.py"""

    def setUp(self):
        """Call all the functions and test them separately."""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = pr.get_project_data(
            self.repo_dicts)

    def test_get_response(self):
        """Test if we get a valid response."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """Test if we are getting the data we think we are."""
        # Get dicts for 30 repos.
        self.assertEqual(len(self.repo_dicts), 30)

        # Repos should have required keys.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()
