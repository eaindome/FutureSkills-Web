# services/recommendation_service.py
import random
from typing import List, Optional
from models import AutomationRiskResponse, GreenJob, ReskillingCourse, SideHustle, UserDB
from uuid import UUID

def mock_get_risk_score(job_title: str) -> tuple[int, str]:
    """Mocks automation risk based on job title."""
    job_title_lower = job_title.lower()
    if "cashier" in job_title_lower or "retail" in job_title_lower:
        return 75, "Cashier jobs face high automation risk due to self-checkout technology and online retail."
    elif "teacher" in job_title_lower or "educator" in job_title_lower:
        return 50, "Teaching roles have moderate automation risk, with technology assisting but human interaction remaining key."
    else:
        return 60, "This job has a moderate automation risk, typical for many roles impacted by technology."

def mock_get_green_jobs(job_title: str, interests: Optional[str]) -> List[GreenJob]:
    """Mocks green job recommendations."""
    # This logic is copied directly from the original main.py mock section
    jobs: List[GreenJob] = []
    job_title_lower = job_title.lower()
    interests_lower = interests.lower() if interests else ""

    if "cashier" in job_title_lower or "retail" in job_title_lower:
        jobs.append(GreenJob(
            title="Solar Sales Support Specialist",
            growthRate=random.randint(10, 20),
            skillMatch="Uses your customer service and sales skills",
            description="Assist customers with solar panel purchases and installation scheduling.",
            salary="$45,000 - $60,000"
        ))
        if "environment" in interests_lower or "eco" in interests_lower:
             jobs.append(GreenJob(
                title="Eco-Retail Coordinator",
                growthRate=random.randint(8, 15),
                skillMatch="Uses your inventory and customer interaction experience",
                description="Manage sustainable product lines and assist customers in an eco-friendly retail setting.",
                salary="$42,000 - $55,000"
            ))
        else: # Default second option if no specific environmental interest
             jobs.append(GreenJob(
                title="Community Recycling Program Assistant",
                growthRate=random.randint(5, 10),
                skillMatch="Uses your organizational and public interaction skills",
                description="Help manage local recycling initiatives and educate the public.",
                salary="$35,000 - $45,000"
            ))

    elif "teacher" in job_title_lower or "educator" in job_title_lower:
        jobs.append(GreenJob(
            title="Environmental Education Program Manager",
            growthRate=random.randint(10, 18),
            skillMatch="Leverages your teaching and program management abilities",
            description="Develop and deliver educational programs on environmental topics for schools or community groups.",
            salary="$50,000 - $70,000"
        ))
        jobs.append(GreenJob(
            title="Sustainability Training Coordinator",
            growthRate=random.randint(12, 25),
            skillMatch="Uses your training and communication skills",
            description="Coordinate and deliver training sessions for businesses on sustainable practices.",
            salary="$55,000 - $75,000"
        ))

    else: # Default recommendations for others
        jobs.append(GreenJob(
            title="Green Building Consultant Assistant",
            growthRate=random.randint(10, 20),
            skillMatch="Adaptable to new industry knowledge",
            description="Assist in consulting projects for sustainable construction and building practices.",
            salary="$40,000 - $55,000"
        ))
        jobs.append(GreenJob(
            title="Renewable Energy Project Administrator",
            growthRate=random.randint(15, 25),
            skillMatch="Uses organizational and administrative skills",
            description="Provide administrative support for solar, wind, or other renewable energy projects.",
            salary="$45,000 - $60,000"
        ))

    # Shuffle and return max 2 for variety in demo
    random.shuffle(jobs)
    return jobs[:2]

def mock_get_reskilling_courses(job_title: str, interests: Optional[str]) -> List[ReskillingCourse]:
    """Mocks reskilling course recommendations."""
    # This logic is copied directly from the original main.py mock section
    courses: List[ReskillingCourse] = []
    job_title_lower = job_title.lower()
    interests_lower = interests.lower() if interests else ""

    if "cashier" in job_title_lower or "retail" in job_title_lower:
        courses.append(ReskillingCourse(
            title="Coursera: Sustainable Business Practices",
            provider="Coursera",
            duration="6 weeks",
            skills="Sustainability, customer engagement, business ethics",
            link="https://www.coursera.org/courses?query=sustainable%20business%20practices" # Example link
        ))
        if "environment" in interests_lower or "eco" in interests_lower or "green" in interests_lower:
             courses.append(ReskillingCourse(
                title="edX: Solar Energy Fundamentals",
                provider="edX",
                duration="8 weeks",
                skills="Renewable energy, solar technology, basic sales principles",
                link="https://www.edx.org/learn/solar-energy" # Example link
            ))
        else:
            courses.append(ReskillingCourse(
                title="Coursera: Introduction to Sales",
                provider="Coursera",
                duration="4 weeks",
                skills="Sales techniques, customer relationship management",
                link="https://www.coursera.org/courses?query=introduction%20to%20sales" # Example link
            ))

    elif "teacher" in job_title_lower or "educator" in job_title_lower:
        courses.append(ReskillingCourse(
            title="Coursera: Climate Change Education",
            provider="Coursera",
            duration="7 weeks",
            skills="Environmental education, climate science communication, pedagogy",
            link="https://www.coursera.org/courses?query=climate%20change%20education" # Example link
        ))
        courses.append(ReskillingCourse(
            title="edX: Urban Sustainability",
            provider="edX",
            duration="9 weeks",
            skills="Urban planning, environmental policy, sustainable development",
            link="https://www.edx.org/learn/sustainable-development" # Example link
        ))
    else: # Default courses for others
        courses.append(ReskillingCourse(
            title="Coursera: Circular Economy",
            provider="Coursera",
            duration="5 weeks",
            skills="Circular economy principles, sustainable design",
            link="https://www.coursera.org/courses?query=circular%20economy" # Example link
        ))
        courses.append(ReskillingCourse(
            title="edX: Introduction to Environmental Science",
            provider="edX",
            duration="6 weeks",
            skills="Environmental systems, ecological principles",
            link="https://www.edx.org/learn/environmental-science" # Example link
        ))

    # Shuffle and return max 2
    random.shuffle(courses)
    return courses[:2]

def mock_get_side_hustles(job_title: str, interests: Optional[str]) -> List[SideHustle]:
    """Mocks side hustle recommendations."""
    # This logic is copied directly from the original main.py mock section
    hustles: List[SideHustle] = []
    job_title_lower = job_title.lower()
    interests_lower = interests.lower() if interests else ""

    if "cashier" in job_title_lower or "retail" in job_title_lower:
        if "environment" in interests_lower or "eco" in interests_lower:
            hustles.append(SideHustle(
                title="Etsy Eco-Crafts",
                description="Sell handmade sustainable crafts (e.g., upcycled items, eco-friendly candles) on Etsy.",
                skills="Creativity, crafting, online selling, customer service",
                earnings=f"${random.randint(300, 800)*random.choice([1, 2])} - ${random.randint(1000, 2500)*random.choice([1, 2])}/month" # Randomize range a bit
            ))
            hustles.append(SideHustle(
                title="Green Blogging / Social Media Content",
                description="Create content about sustainability, zero waste, or eco-friendly living.",
                skills="Writing, research, social media marketing",
                earnings=f"${random.randint(100, 300)*random.choice([1, 2])} - ${random.randint(500, 1500)*random.choice([1, 2])}/month"
            ))
        else: # Default hustles if no specific environmental interest
             hustles.append(SideHustle(
                title="Online Reselling (Sustainable Goods)",
                description="Buy and resell second-hand clothing or vintage items online.",
                skills="Eye for value, online marketplaces, photography, customer service",
                earnings=f"${random.randint(400, 900)*random.choice([1, 2])} - ${random.randint(1200, 2800)*random.choice([1, 2])}/month"
            ))
             hustles.append(SideHustle(
                title="Local Errand Service (using sustainable transport)",
                description="Offer delivery or errand services in your neighborhood using a bike or walking.",
                skills="Reliability, organization, knowledge of local area, physical fitness",
                earnings=f"${random.randint(200, 500)*random.choice([1, 2])} - ${random.randint(800, 2000)*random.choice([1, 2])}/month"
            ))


    elif "teacher" in job_title_lower or "educator" in job_title_lower:
        hustles.append(SideHustle(
            title="Online Environmental Tutoring",
            description="Offer tutoring in science or environmental subjects to students online.",
            skills="Subject matter expertise, online teaching tools, communication",
            earnings=f"${random.randint(300, 800)*random.choice([1, 2])} - ${random.randint(1000, 2500)*random.choice([1, 2])}/month"
        ))
        hustles.append(SideHustle(
            title="Workshop Facilitator (Sustainable Living)",
            description="Lead local workshops on topics like composting, urban gardening, or DIY eco-products.",
            skills="Teaching, presentation, subject matter knowledge",
            earnings=f"${random.randint(200, 600)*random.choice([1, 2])} - ${random.randint(700, 1800)*random.choice([1, 2])}/month"
        ))

    else: # Default hustles for others
        hustles.append(SideHustle(
            title="Freelance Green Copywriting",
            description="Write articles, blog posts, or marketing content for environmentally focused businesses.",
            skills="Writing, research, understanding of green industries",
            earnings=f"${random.randint(400, 1000)*random.choice([1, 2])} - ${random.randint(1500, 3500)*random.choice([1, 2])}/month"
        ))
        hustles.append(SideHustle(
            title="Sustainable Product Affiliate Marketing",
            description="Promote eco-friendly products online and earn commission.",
            skills="Online marketing, content creation, product reviews",
            earnings=f"${random.randint(100, 400)*random.choice([1, 2])} - ${random.randint(600, 2000)*random.choice([1, 2])}/month"
        ))

    # Shuffle and return max 2
    random.shuffle(hustles)
    return hustles[:2]