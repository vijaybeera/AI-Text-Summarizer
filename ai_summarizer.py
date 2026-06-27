# A simple Text Summarizer using basic Python logic

def generate_summary(text):
    # simple list of common words to ignore
    stop_words = ["the", "a", "an", "and", "but", "is", "are", "was", "were", "in", "on", "at", "to", "for", "with", "it", "of", "this", "that", "my", "you", "he", "she", "they"]

    # cleaning text a bit and converting to lowercase to count words
    words = text.lower().split()
    
    # 1. Counting how many times each important word repeats
    word_counts = {}
    for word in words:
        # removing dots and commas from words
        word = word.replace(".", "").replace(",", "").strip()
        if word not in stop_words and len(word) > 2:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

    # 2. Splitting the full text into sentences using simple dot (.)
    sentences = text.split(".")
    sentence_scores = {}

    # 3. Giving score to each sentence based on important words
    for idx, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if len(sentence) < 5:  # skip empty or very small lines
            continue
            
        score = 0
        for word in sentence.lower().split():
            if word in word_counts:
                score += word_counts[word]
        
        # saving sentence score with its index to maintain order later
        sentence_scores[idx] = score

    # 4. Sorting sentences based on highest score and picking top 3 lines
    sorted_indexes = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    
    # putting the top sentences back in original order so it reads nicely
    sorted_indexes.sort()
    
    final_summary = []
    for idx in sorted_indexes:
        final_summary.append(sentences[idx].strip() + ".")
        
    return " ".join(final_summary)

def main():
    print("--- MY AI TEXT SUMMARIZER ---")
    print("Enter or paste your long paragraph below:")
    user_text = input().strip()

    if len(user_text) < 30:
        print("Error: Please enter a longer text to summarize!")
        return

    print("\nProcessing your summary...")
    summary = generate_summary(user_text)
    
    print("\n--- Summary Result ---")
    print(summary)

if __name__ == "__main__":
    main()
