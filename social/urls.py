from .models import Post
from .views import PostListView,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AdddisLike, UserSearch, ListFollower, AddLikeComment, AdddisLikeComment, CommentReplyView, PostNotification, FollowNotification, RemoveNotification, ListThreads, CreateThreads, ThreadView, CreateMessage, ThreadNotification, Explore
from django.urls import path


urlpatterns = [
    #link to go to post list home page
    path('', PostListView.as_view(), name='post-list'),

    #link to go to post's detail page
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),

    #link to go to update the post page 
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),

    #link to delete the post from the page
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),

    #link to delete the comment from the page
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),

    #link to like and dislike the comment
    path('post/<int:post_pk>/comment/<int:pk>/like', AddLikeComment.as_view(), name='like-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AdddisLikeComment.as_view(), name='dislike-comment'),

    #link to reply on the comment
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='reply-comment'),

    #link to profile page of active logged in user
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),

    #link to update the profile of the active logged in user
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    
    #link to add new follower to follower list
    path('profile/<int:pk>followers/add', AddFollower.as_view(), name='add-follower'),

    #link to remove follower from follower list
    path('profile/<int:pk>followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    
    #link to like and dislike the post
    path('post/<int:pk>/like', AddLike.as_view(), name='like-post'),
    path('post/<int:pk>/dislike', AdddisLike.as_view(), name='dislike-post'),

    #link to add search user profile
    path('search/', UserSearch.as_view(), name='search-profile'),

    #link to get the follower list of the user
    path('profile/<int:pk>/followers', ListFollower.as_view(), name='follower-list'),

    #links to direct to specific destination from different types of notifications
    path('notification/<int:notification_pk>/post/<int:post_pk>/', PostNotification.as_view(), name="post-notification"),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>/', FollowNotification.as_view(), name="follow-notification"),
    path('notification/<int:notification_pk>/thread/<int:object_pk>/', ThreadNotification.as_view(), name="thread-notification"),

    #link to delete a notification
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='delete-notification'),

    #link to go to message inbox
    path('inbox/', ListThreads.as_view(), name='inbox'),

    #link to create new thread
    path('inbox/create-thread', CreateThreads.as_view(), name='create-thread'),

    #link to go to specific thread
    path('thread/<int:pk>', ThreadView.as_view(), name='thread'),

    #link to send message in the thread
    path('thread/<int:pk>/messages', CreateMessage.as_view(), name='create-message'),

    #link to explore posts and comment with desired tags
    path('explore/', Explore.as_view(), name='explore'),

]
