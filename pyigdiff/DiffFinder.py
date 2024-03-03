class DiffFinder:
    def __init__(self, followers, following):
        self.__validate_args(followers, 'followers')
        self.__validate_args(following, 'following')
        self.followers = self.__fetch_usernames(followers)
        self.following = self.__fetch_usernames(following['relationships_following'])

    def __validate_args(self, json_file, json_name):
        if json_file is None:
            raise ValueError('json %s file was not opened successfully', json_name)

    def __fetch_usernames(self, usernames):
        return set(sorted([username['string_list_data'][0]['value'] for username in usernames]))

    def generate_report(self):
        followers_not_in_following = self.followers - self.following
        following_not_in_followers = self.following - self.followers
        report = ""
        report += "The user is not following these accounts:\n"
        for name in followers_not_in_following:
            report += " > " + name + "\n"
        report += "\n"
        report += "These accounts are not following the user:\n"
        for name in following_not_in_followers:
            report += " > " + name + "\n"
        return report
