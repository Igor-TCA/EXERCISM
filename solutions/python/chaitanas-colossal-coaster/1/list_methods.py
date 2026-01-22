"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number."""
    queue_map ={0: normal_queue, 1: express_queue}
    
    chosen_queue = queue_map[ticket_type]
    chosen_queue.append(person_name)
    
    return chosen_queue

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index)."""
    if friend_name in queue: 
        return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue."""
    queue.insert(index, person_name)
    return queue
    
def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name."""
    person_index = queue.index(person_name)
    queue.pop(person_index)
    return queue

def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue."""
    namefellows = queue.count(person_name)
    return namefellows
    
def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name."""
    return queue.pop()
    
def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result."""
    return sorted(queue)