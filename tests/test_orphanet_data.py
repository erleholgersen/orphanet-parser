from orphanet_parser import OrphanetData


def test_natural_history():
    parser = OrphanetData(version="2024-07")
    df = parser.natural_history()

    assert len(df['orphacode'].unique()) == len(df)
