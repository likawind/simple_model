class Function:
    def predict(self, review, wine):
        review['color'] = wine['color'].iloc[0]
        return review