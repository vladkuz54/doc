import os
import csv
import random
from datetime import datetime, timedelta 

class CSVGenerator:
    def __init__(self, filename='courses.csv', num_rows=1000):
        self.filename = filename
        self.num_rows = num_rows

    def random_course(self):
        titles = ["Python for Beginners", "Advanced Java", "Data Science 101", "Web Development", "Machine Learning"]
        descriptions = [
            "Learn Python basics", "Master Java programming", "Intro to Data Science", "Build modern websites", "ML for everyone"
        ]
        difficulties = ["Beginner", "Intermediate", "Advanced"]
        languages = ["English", "Ukrainian", "Spanish"]
        idx = random.randint(0, len(titles)-1)
        return {
            "course_title": titles[idx],
            "course_description": descriptions[idx],
            "course_difficulty": random.choice(difficulties),
            "course_language": random.choice(languages)
        }

    def random_module(self, order):
        module_titles = ["Introduction", "Basics", "Control Flow", "Functions", "Final Quiz"]
        return {
            "module_title": random.choice(module_titles),
            "module_order_index": order,
            "module_is_locked": random.choice([True, False])
        }

    def random_material(self):
        material_types = ["Video", "Text", "Test"]
        mtype = random.choice(material_types)
        base = {
            "material_title": "",
            "material_type": mtype,
            "estimated_time": random.randint(5, 30),
            "is_mandatory": random.choice([True, False]),
            "release_date": (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        }
        if mtype == "Video":
            base.update({
                "material_title": "Lesson Video",
                "video_url": f"https://edx.org/v{random.randint(1,100)}",
                "video_is_watched": random.choice([True, False]),
                "video_duration_seconds": random.randint(60, 1200),
                "video_has_subtitles": random.choice([True, False]),
                "text_body": "",
                "text_is_read": "",
                "text_reading_time_min": "",
                "text_is_downloadable": "",
                "text_word_count": "",
                "test_score": "",
                "test_passing_score": "",
                "test_is_passed": "",
                "test_attempts_limit": "",
                "test_time_limit": ""
            })
        elif mtype == "Text":
            base.update({
                "material_title": "Theory Text",
                "video_url": "",
                "video_is_watched": "",
                "video_duration_seconds": "",
                "video_has_subtitles": "",
                "text_body": "Lorem ipsum dolor sit amet...",
                "text_is_read": random.choice([True, False]),
                "text_reading_time_min": random.randint(5, 15),
                "text_is_downloadable": random.choice([True, False]),
                "text_word_count": random.randint(100, 1000),
                "test_score": "",
                "test_passing_score": "",
                "test_is_passed": "",
                "test_attempts_limit": "",
                "test_time_limit": ""
            })
        else: 
            base.update({
                "material_title": "Final Quiz",
                "video_url": "",
                "video_is_watched": "",
                "video_duration_seconds": "",
                "video_has_subtitles": "",
                "text_body": "",
                "text_is_read": "",
                "text_reading_time_min": "",
                "text_is_downloadable": "",
                "text_word_count": "",
                "test_score": random.randint(0, 100),
                "test_passing_score": 80,
                "test_is_passed": random.choice([True, False]),
                "test_attempts_limit": random.randint(1, 5),
                "test_time_limit": random.randint(10, 60)
            })
        return base

    def generate_csv(self):
        filepath = f"{self.filename}"
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "course_title","course_description","course_difficulty","course_language",
                "module_title","module_order_index","module_is_locked",
                "material_title","material_type","estimated_time","is_mandatory","release_date",
                "video_url","video_is_watched","video_duration_seconds","video_has_subtitles",
                "text_body","text_is_read","text_reading_time_min","text_is_downloadable","text_word_count",
                "test_score","test_passing_score","test_is_passed","test_attempts_limit","test_time_limit"
            ])
            for i in range(self.num_rows):
                course = self.random_course()
                module = self.random_module(order=random.randint(1, 5))
                material = self.random_material()
                row = [
                    course["course_title"],
                    course["course_description"],
                    course["course_difficulty"],
                    course["course_language"],
                    module["module_title"],
                    module["module_order_index"],
                    module["module_is_locked"],
                    material["material_title"],
                    material["material_type"],
                    material["estimated_time"],
                    material["is_mandatory"],
                    material["release_date"],
                    material["video_url"],
                    material["video_is_watched"],
                    material["video_duration_seconds"],
                    material["video_has_subtitles"],
                    material["text_body"],
                    material["text_is_read"],
                    material["text_reading_time_min"],
                    material["text_is_downloadable"],
                    material["text_word_count"],
                    material["test_score"],
                    material["test_passing_score"],
                    material["test_is_passed"],
                    material["test_attempts_limit"],
                    material["test_time_limit"]
                ]
                writer.writerow(row)
        print(f'Generated {self.num_rows} rows in {filepath}')

generator = CSVGenerator(filename='courses.csv', num_rows=1000)