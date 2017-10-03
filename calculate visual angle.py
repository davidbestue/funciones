
# coding: utf-8

# In[4]:


from math import atan, degrees
import easygui


# In[5]:


#box to enter stim size and distance

#stim size
#It takes into account that you fixate in the center of the stim
stim_size = easygui.enterbox(msg='Enter the stim size (cm)', title='value')
stim_size=int(stim_size)

#distance from the eye to the stim. It is not important wether there is a mirror or not. It does not affect.
# If there is a mirror: distance = dist_eye_mirror + dist_mirror_
distance = easygui.enterbox(msg='Enter the distance (cm)', title='value')
distance=int(distance)



# In[6]:


visual_angle = degrees(  atan( (float(stim_size)/2)  / float(distance)  )    )  *  2

visual_angle=round(visual_angle, 3)

print visual_angle

