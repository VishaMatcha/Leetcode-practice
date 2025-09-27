class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = -int(2 ** 31)

        i = 0
        while(i < len(points) - 2):

            j = i + 1
            while(j < len(points) - 1):

                k = j + 1
                while(k < len(points)):

                    temp_area = 0.5 * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1])  + points[k][0] * (points[i][1] - points[j][1]))                  
                    
                    if(temp_area > max_area):
                        max_area = temp_area

                    k += 1

                j += 1

            i += 1

        return max_area