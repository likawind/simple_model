def join(self, review, wine):
    review['color'] = wine['color'].iloc[0]
    return review