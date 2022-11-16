import Extract
import Transform
import Load

if __name__ == "__main__":

    # Extract
    print('[Extract] Start')
    print('[Extract] Connecting to API')
    data = Extract.connect_api()

    print('[Extract] Collecting articles')
    article_df = Extract.extract_articles(data)

    print('[Extract] Collecting videos')
    video_df = Extract.extract_videos(data)

    print('[Extract] End.\n\n')

    # Transform
    print('[Transform] Start')
    print('[Transform] Transforming articles')
    article_df = Transform.transform_article(article_df)

    print('[Transform] Transforming videos')
    video_df = Transform.transform_video(video_df)

    print('[Transform] Consolidating data')
    df = Transform.consolidate(article_df, video_df)

    print('[Transform] Cleaning data')
    df['cleanedText'] = df['combinedText'].apply(Transform.cleaning)
    df.drop('combinedText', axis=1, inplace=True)

    print('[Transform] End.\n\n')

    # Load
    print('[Load] Start')
    print('[Load] Saving data to csv')
    Load.load_to_csv(df)

    print('[Load] Data saved as "Bloomberg_data.csv"')
    print('[Load] End.')
