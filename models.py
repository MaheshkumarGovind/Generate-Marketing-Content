def generate_marketing_content(topic, format):
    # Based on the topic and format, generate the marketing content
    if format == 'linkedin post':
        content = f"Excited to share insights on {topic}! 🚀 With its innovative capabilities, {topic} is revolutionising various industries, from creative arts to healthcare. Its potential to generate realistic images, text, and even music is reshaping the way we create and interact with technology. Let's explore the endless possibilities and opportunities this cutting-edge technology offers. #{topic.replace(' ', '')} #Innovation #TechRevolution 🤖💡"
    else:
        content = "Unsupported format"
    
    return content

